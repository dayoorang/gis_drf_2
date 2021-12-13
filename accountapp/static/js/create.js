


function send_input() {
    axios.post('/accounts/create/', {
    input_data: document.getElementById('input_data').value
  })
  .then(function (response) {
    console.log(response);

    document.getElementById('text').innerHTML = response.data['text'];
    document.getElementById('new_model_created_at').innerHTML = response.data['created_at'];

    document.getElementById('new_model_list').innerHTML += '<h5>'+response.data['text']+'</h5>'
    document.getElementById('new_model_list').innerHTML += '<p>'+response.data['created_at']+'</p>'

  })
  .catch(function (error) {
    console.log(error);
  });
}