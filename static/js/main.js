console.log("hello")

const helloWorldBox = document.getElementById('hello-world')


$.ajax({
    type: 'GET', 
    url: '/polls/hello-world/', // wtf
    success: function(response){
        console.log('success', response)
        helloWorldBox.textContent = response.text // pega o texto do response que é o json
    },
    error: function(error){
        console.log('error', error)
    }
})


$.ajax({
    type: 'GET',
    url:  '/polls/data/',
    success: function(response){
        console.log(response)
        const data = JSON.parse(response.data)
        console.log(data)
    },
    error: function(error){
        console.log(error)
    }
})