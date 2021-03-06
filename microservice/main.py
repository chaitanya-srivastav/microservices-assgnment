# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask, render_template, request, jsonify, abort, redirect
from flask import make_response
from flasgger import Swagger
import os, logging
from flask_httpauth import HTTPBasicAuth
import requests
import requests_toolbelt.adapters.appengine
# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()

app = Flask(__name__)
Swagger(app)
auth = HTTPBasicAuth()

users = {
    "micro": "service",
}

@app.route('/')
def index():
    return redirect("/apidocs/", code=302)

@app.route('/api/nextflight')
@auth.login_required
def nextFlight():
    """
    Customers flying for the next 7 days API
    Customers who will fly for the next 7 days based on CRM team searched customer's departure station API
    ---
    tags:
      - Next Flight Information API
    parameters:
      - name: DepartureStationCode
        in: query
        required: true
        type: string
        description: departure code
    responses:
      500:
        description: Error!
      200:
        description: Next Flight Information
        schema:
          id: FlightInfo
          properties:
            key_id:
              type: string
              default: DMK
            contacts:
              type: array
              items:
                type: object
                properties:
                  2:
                    type: string
                    default: VTEDMK
                  source_id:
                    type: string
                    default: 111
    """
    microuser = os.environ["MICROUSERNAME"]
    micropass = os.environ["MICROPASSWORD"]
    url = 'https://us-central1-airasiawebanalytics.cloudfunctions.net/interviewAPIdata/nextflight'
    print 'Trying to hit: ' + url
    headers = {'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    r = requests.get(url, auth=(microuser, micropass), headers=headers)
    print r
    all_flights_info = r.json()
    dsc = request.args.get('DepartureStationCode')
    filter_based_on_input = [{"2": flight_info["NEXT_ARRIVALSTATION"] + dsc, "source_id": flight_info["customerID"]} for flight_info in all_flights_info if flight_info["NEXT_DEPARTURESTATION"] == dsc]
    resp = {"key_id": dsc, "contacts": filter_based_on_input}
    return jsonify(resp)

@auth.verify_password
def verify_password(username, password):
    if username in users:
        passwd = users.get(username)
        if password == passwd:
            return True
        else:
            return False
    if not username:
        return False


if __name__ == "__main__":
    app.run(debug=True)
