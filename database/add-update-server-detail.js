const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/serverDB', {useNewUrlParser: true, useUnifiedTopology: true});

const ResourceAllocation = require('./database/mongodb-schema');

// Creating a new server document with all fields mandatory
const newResourceAllocation = new ResourceAllocation({
    serverName: "Server1",
    bmcURL: "BMC1",
    bmcUserName: "root",
    bmcPassword: "0penBmc",
    osHostname: "hostname",
    osUserName: "amd",
    osPassword: "amd1234!",
    location: "ATS",
    floor: "12th",
    labName: "Andromeda",
    rack: "Rack 5",
    numberOfNICsInstalled: 2,
    nicsModel: ["IntelE810", "NVIDIA CX7"],
    connectedToTrafficGen: true,
    trafficGen: "Xena",
    trafficGenModule: "0",
    trafficGenPort: "0,1",
    nicConnectedToTrafficGen: "NVIDIA CX7",
    serverConnectionsToAnotherServer: ["Yes"],
    peerServerBMC: "BMC2",
    peerServerHostname: "hostname"
});

newServer.save().then(() => console.log("Server added successfully")).catch(err => console.error(err));
