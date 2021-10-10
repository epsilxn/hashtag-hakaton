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
                    $nuxt.$store.dispatch('auth',res.data.auth_token)
                    axios.get("http://127.0.0.1:8000/auth/users/me/", 
                        { headers: { 'Authorization': `Token ${this.$store.state.token}` } })
                        .then((resp) => {
                            axios.get(`http://127.0.0.1:8000/api/me/${resp.data.id}`).then((resp) => {
                                $nuxt.$store.dispatch('setStaff', resp.data.is_staff)
                                document.cookie = `token=${String(this.$store.state.token)}`;
                                console.log(document.cookie)
                                this.$router.push('lk/')
                            })
                        })
                })
            }
            else{
                this.message='Все поля должны быть заполнены'
            }
            
        }
    }
}
</script>