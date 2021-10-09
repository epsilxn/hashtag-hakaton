<template>
    <div class="auth">
        <Form
            @onSubmit="onSubmit"
            :login="false"
            :message="message"/>
    </div>
</template>


<script>
import Form from '@/components/auth/Form.vue'
import axios from 'axios'
export default {
    data(){
        return{
            message: null,
            user:{
                email:'',
                password: '',
                login:'',
                name: '',
                surname: '',
                patronymic: ''
            }
        }
    },
    components:{
        Form
    },
    methods:{
        onSubmit(user){
            if(user.email!='' 
                && user.login!='' 
                && user.password.length>3
                && user.name!=''
                && user.surname!=''
            ){
                axios.post('http://127.0.0.1:8000/auth/users', {
                    first_name: user.name,
                    last_name: user.surname,
                    patronymic: user.patronymic,
                    username: user.login,
                    email: user.email
                })
                .then((resp)=>{
                    console.log(resp)
                })
                this.message=null
            }
            else{
                this.message='Все поля должны быть заполнены'
            }
            
        }
    }
}
</script>