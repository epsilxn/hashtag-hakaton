<template>
    <form class="main_form" @submit.prevent="onSubmit">
        <div v-if="login" class="form_head">Авторизация</div>
        <div v-else class="form_head">Регистрация</div>
        <div class="form_body">
            <div v-if="message" class="form_message">{{message}}</div>
            <input 
                placeholder="Введите почту" 
                class="form_input" 
                type="email" 
                name="email" 
                id="email"
                v-model="user.email"/>
            <input placeholder="Ваш пароль"  
                class="form_input" 
                type="password" 
                name="password" 
                id="password"
                v-model="user.password"/>
            <button v-if="login" class="form_button">Войти</button>
            <button v-else class="form_button">Сохранить</button>
        </div>
    </form>
</template>

<script>
export default {
    data(){
        return{
            user:{
                email:'',
                password:''
            },
        }
    },
    props:{
        message:{
            type: String,
            default: null
        },
        login:{
            type: Boolean,
            default: true
        }
    },
    methods:{
        onSubmit(){
            this.$emit('onSubmit', this.user)
        }
    }
}
</script>