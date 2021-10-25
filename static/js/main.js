console.log("hello")

const helloWorldBox = document.getElementById('hello-world')
const postsBox = document.getElementById('posts-box')
const spinnerBox = document.getElementById('spinner-box')

const postForm = document.getElementById('post-form')
const name = document.getElementById('id_name')
const email = document.getElementById('id_email')
const bio = document.getElementById('id_bio')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log('csrf', csrf)

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
    url:  `/polls/data/`,
    success: function(response){
        console.log(response)
        // const data = JSON.parse(response.data)
        const data = response.data
        setTimeout(()=>{
            spinnerBox.classList.add('not-visible')
            console.log(data)
            helloWorldBox.textContent = "hello world 2 "
        }, 1000)

        data.forEach(element => {
            postsBox.innerHTML += ` 
            <div class="card" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title">${element.name}</h5>
                    <p class="card-text">${element.email}</p>
                    <div class="card-footer">
                        <div class="row">
                            <div class="col-4">
                                <a href="#" class="btn btn-primary">Details</a>
                            </div>
                            <div class="col-4">
                                <a href="#" class="btn btn-primary">Like</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            `
        });


    },
    error: function(error){
        console.log(error)
    }
})


postForm.addEventListener('submit', e=>{
    e.preventDefault()
    var formData = $("post-form").serialize().split("&");
    console.log("aqui" + formData );
    $.ajax({
        type: 'POST',
        url: '',
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
            'name': name.value,
            'email': email.value,
            'bio': bio.value
        },
        success: function(response){
            console.log(response)

        },
        error: function(erro){
            console.log(error)
        }
    })
})