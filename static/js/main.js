console.log("hello")


$.ajax({
    type: 'GET', 
    url: '/polls/hello-world/', // wtf
    success: function(response){
        console.log('success', response)
    },
    error: function(error){
        console.log('error', error)
    }
})