<template>
    <section class="auth">
        <Form
            @onSubmit="onSubmit"
            :login="true"
            :message="message"/>
    </section>
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
                password: ''
            }
        }
    },
    components:{
        Form
    },
    methods:{
        onSubmit(user){
            if(user.login!='' && user.password.length>3){
                this.user = user
                this.message=null
                
                axios.post('http://127.0.0.1:8000/auth/token/login/',{
                    username: this.user.login,
                    password: this.user.password
                }).then((res)=>{
                    this.$store.commit('setStaff')
                    $nuxt.$store.dispatch('setToken',res.data.auth_token)
                    console.log(this.$store.state.token)
                })
            }
            else{
                this.message='Все поля должны быть заполнены'
            }
            
        }
    }
}
</script>