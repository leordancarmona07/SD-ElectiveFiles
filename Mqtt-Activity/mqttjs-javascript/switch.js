// var client  = mqtt.connect({ host:'test.mosquitto.org', port: 8081})
// or
// var client  = mqtt.connect('wss://test.mosquitto.org:8081/mqtt')

// var client  = mqtt.connect({ host:'mqtt.eclipse.org/mqtt', port: 443})
// or
// var client  = mqtt.connect('wss://mqtt.eclipse.org:443/mqtt')

var broker = 'wss://mqtt.eclipse.org:443/mqtt';
var client  = mqtt.connect(broker);

var status_header = document.getElementById('status-header')

client.on('connect', function () {
    status_header.innerHTML = 'Connected to '+broker; 
    console.log('Connected to '+broker)
    client.subscribe('junrey/messages', function (err) {
        if (!err) {
            client.publish('junrey/messages', 'Hello mqtt')
        }
    })
})

// client.on('message', function (topic, message) {
//   // message is Buffer
//   console.log(message.toString())
// //   client.end()
// })

// var pub_button = document.getElementById('pub-button');
// var pub_input = document.getElementById('pub-input');
// pub_button.addEventListener('click', () => {
//   // console.log('clicked');
//   // console.log(pub_input.value);
//   client.publish('junrey/messages', pub_input.value)
//   pub_input.value = "";
// })

var pub_switch = document.getElementById('pub-switch');
var value = document.getElementById('pub-switch').value
pub_switch.onclick = () => {
    console.log(pub_switch.checked)
    console.log(value)
    client.publish('leordan-switch', JSON.stringify({checker: String(pub_switch.checked),pixel:value}))
}
var pub_switch1 = document.getElementById('pub-switch1');
var value1 = document.getElementById('pub-switch1').value
pub_switch1.onclick = () => {
    console.log(pub_switch1.checked)
    console.log(value1)
    client.publish('leordan-switch', JSON.stringify({checker: String(pub_switch1.checked),pixel:value1}))
}
var pub_switch2 = document.getElementById('pub-switch2');
var value2 = document.getElementById('pub-switch2').value
pub_switch2.onclick = () => {
    console.log(pub_switch2.checked)
    console.log(value2)
    client.publish('leordan-switch', JSON.stringify({checker: String(pub_switch2.checked),pixel:value2}))
}
var pub_switch3 = document.getElementById('pub-switch3');
var value3 = document.getElementById('pub-switch3').value
pub_switch3.onclick = () => {
    console.log(pub_switch3.checked)
    console.log(value3)
    client.publish('leordan-switch', JSON.stringify({checker: String(pub_switch3.checked),pixel:value3}))
}
var pub_switch4 = document.getElementById('pub-switch4');
var value4 = document.getElementById('pub-switch4').value
pub_switch4.onclick = () => {
    console.log(pub_switch4.checked)
    console.log(value4)
    client.publish('leordan-switch', JSON.stringify({checker: String(pub_switch4.checked),pixel:value4}))
}
var pub_switch5 = document.getElementById('pub-switch5');
var value5 = document.getElementById('pub-switch5').value
pub_switch5.onclick = () => {
    console.log(pub_switch5.checked)
    console.log(value5)
    client.publish('leordan-switch', JSON.stringify({checker: String(pub_switch5.checked),pixel:value5}))
}
var pub_switch6 = document.getElementById('pub-switch6');
var value6 = document.getElementById('pub-switch6').value
pub_switch6.onclick = () => {
    console.log(pub_switch6.checked)
    console.log(value6)
    client.publish('leordan-switch', JSON.stringify({checker: String(pub_switch6.checked),pixel:value6}))
}
var pub_switch7 = document.getElementById('pub-switch7');
var value7 = document.getElementById('pub-switch7').value
pub_switch7.onclick = () => {
    console.log(pub_switch7.checked)
    console.log(value7)
    client.publish('leordan-switch', JSON.stringify({checker: String(pub_switch7.checked),pixel:value7}))
}
var pub_switch8 = document.getElementById('pub-switch8');
var value8 = document.getElementById('pub-switch8').value
pub_switch8.onclick = () => {
    console.log(pub_switch8.checked)
    console.log(value8)
    client.publish('leordan-switch', JSON.stringify({checker: String(pub_switch8.checked),pixel:value8}))
}
var pub_switch9 = document.getElementById('pub-switch9');
var value9 = document.getElementById('pub-switch9').value
pub_switch9.onclick = () => {
    console.log(pub_switch9.checked)
    console.log(value9)
    client.publish('leordan-switch', JSON.stringify({checker: String(pub_switch9.checked),pixel:value9}))
}