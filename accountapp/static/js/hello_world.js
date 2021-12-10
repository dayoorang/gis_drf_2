
function send_input() {
    axios.post('/accounts/hello_world/', {
    input_data: document.getElementById('input_data').value
  })
  .then(function (response) {
    console.log(response);

    document.getElementById('text').innerHTML = response.data['message'];

  })
  .catch(function (error) {
    console.log(error);
  });
}



<!-- 서버 호출 -->
axios.get('/accounts/hello_world/')
  .then(function (response) {
    // handle success
    console.log(response);

    // 성공했을 경우 어떤 javascript 작업을 할지
    document.getElementById('text').innerHTML = response.data['message'];

  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });

