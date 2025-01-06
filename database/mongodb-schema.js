const mongoose = require('mongoose');

const serverSchema = new mongoose.Schema({
    serverName: {
        type: String,
        required: true
    },
    bmcURL: {
        type: String,
        required: true
    },
    bmcUserName: {
        type: String,
        required: true
    },
    bmcPassword: {
        type: String,
        required: true
    },
    osHostname: {
        type: String,
        required: true
    },
    osUserName: {
        type: String,
        required: true
    },
    osPassword: {
        type: String,
        required: true
    },
    location: {
        type: String,
        required: true
    },
    floor: {
        type: String,
        required: true
    },
    labName: {
        type: String,
        required: true
    },
    rack: {
        type: String,
        required: true
    },
    numberOfNICsInstalled: {
        type: Number,
        required: true
    },
    nicsModel: {
        type: [String],
        required: true
    },
    connectedToTrafficGen: {
        type: Boolean,
        required: true
    },
    trafficGen: {
        type: String,
        required: true
    },
    trafficGenModule: {
        type: String,
        required: true
    },
    trafficGenPort: {
        type: String,
        required: true
    },
    nicConnectedToTrafficGen: {
        type: String,
        required: true
    },
    serverConnectionsToAnotherServer: {
        type: [String],
        required: true
    },
    peerServerBMC: {
        type: String,
        required: true
    },
    peerServerHostname: {
        type: String,
        required: true
    }
});

// Create model from schema
const Server = mongoose.model('ResourceAllocation', serverSchema);

module.exports = ResourceAllocation;
