from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_wtf import FlaskForm

from wtforms import StringField, BooleanField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Optional


from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['server_inventory']
servers_collection = db['servers']

@app.route('/')
def index():
    servers = servers_collection.find()
    return render_template('index.html', servers=servers)

@app.route('/reserve', methods=['POST'])
def reserve():
    server_id = request.form.get('server_id')
    reserve_until = request.form.get('reserve_until')
    
    if server_id and reserve_until:
        servers_collection.update_one(
            {'_id': server_id},
            {'$set': {'reserved_until': reserve_until}}
        )
        return redirect(url_for('index'))
    return "Invalid input", 400

@app.route('/add_server', methods=['POST'])
def add_server():
    model = request.form.get('model')
    status = request.form.get('status')
    if model and status:
        servers_collection.insert_one({
            'model': model,
            'status': status,
            'reserved_until': None
        })
        return redirect(url_for('index'))
    return "Invalid input", 400


class ServerForm(FlaskForm):
    server_name = StringField('Server Name', validators=[DataRequired()])
    bmc_url = StringField('BMC URL', validators=[DataRequired()])
    bmc_username = StringField('BMC Username', validators=[DataRequired()])
    bmc_password = PasswordField('BMC Password', validators=[DataRequired()])
    os_hostname = StringField('OS Hostname', validators=[DataRequired()])
    os_username = StringField('OS Username', validators=[DataRequired()])
    os_password = PasswordField('OS Password', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    floor = StringField('Floor', validators=[DataRequired()])
    lab_name = StringField('Lab Name', validators=[DataRequired()])
    rack_number = StringField('Rack Number', validators=[DataRequired()])
    nics_installed = IntegerField('Number of NICs Installed', validators=[DataRequired()])
    nics_model = StringField('NICs Model', validators=[DataRequired()])
    connected_to_traffic_gen = BooleanField('Connected to Traffic Gen', validators=[DataRequired()])
    traffic_gen = StringField('Traffic Gen', validators=[DataRequired()])
    traffic_gen_module = StringField('Traffic Gen Module', validators=[DataRequired()])
    traffic_gen_port = StringField('Traffic Gen Port', validators=[DataRequired()])
    nic_connected_to_traffic_gen = StringField('NIC Connected to Traffic Gen', validators=[DataRequired()])
    server_connections = StringField('Server Connections to Another Server', validators=[DataRequired()])
    peer_server_bmc = StringField('Peer Server BMC', validators=[DataRequired()])
    peer_server_hostname = StringField('Peer Server Hostname', validators=[DataRequired()])
    submit = SubmitField('Update Server Details')

@app.route('/', methods=['GET', 'POST'])
def update_server():
    form = ServerForm()
    if form.validate_on_submit():
        # Process form data
        server_data = {field.name: field.data for field in form}
        flash('Server details updated successfully!', 'success')
        return redirect(url_for('update_server'))
    return render_template('update_server.html', form=form)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

