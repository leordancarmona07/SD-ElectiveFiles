console.log("index.js");

// var client  = mqtt.connect({ host:'test.mosquitto.org', port: 8081})
// or
// var client  = mqtt.connect('wss://test.mosquitto.org:8081/mqtt')

// var client  = mqtt.connect({ host:'mqtt.eclipse.org/mqtt', port: 443})
// or
var client  = mqtt.connect('wss://mqtt.eclipse.org:443/mqtt')

client.on('connect', function () {
    console.log('connected')
  client.subscribe('junrey/messages', function (err) {
    if (!err) {
      client.publish('junrey/messages', 'Hello mqtt')
    }
  })
})

client.on('message', function (topic, message) {
  // message is Buffer
  console.log(message.toString())
//   client.end()
})

var pub_button = document.getElementById('pub-button');
var pub_input = document.getElementById('pub-input');
pub_button.addEventListener('click', () => {
  // console.log('clicked');
  // console.log(pub_input.value);
  client.publish('junrey/messages', pub_input.value)
  pub_input.value = "";
})