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

export default {
    data(){
        return{
            message: null,
            user:{
                email:'',
                password: '',
                fio: '',
                childs: '',
                photo: ''
            }
        }
    },
    components:{
        Form
    },
    methods:{
        onSubmit(user){
            if(user.email!='' && user.password.length>3){
                console.log(user)
                this.message=null
            }
            else{
                this.message='Все поля должны быть заполнены'
            }
            
        }
    }
}
</script>