<template>
    <form class="main_form" @submit.prevent="onSubmit">
        <div v-if="login" class="form_head">Авторизация</div>
        <div v-else class="form_head">Регистрация</div>
        <div class="form_body">
            <div v-if="message" class="form_message">{{message}}</div>
            <input 
                v-if="!login"
                placeholder="Введите почту" 
                class="form_input" 
                type="email" 
                name="email" 
                id="email"
                v-model="user.email"/>
            <input 
                placeholder="Введите Логин" 
                class="form_input" 
                type="text" 
                name="login" 
                id="login"
                v-model="user.login"/>
            <input placeholder="Ваш пароль"  
                class="form_input" 
                type="password" 
                name="password" 
                id="password"
                v-model="user.password"/>
            <input placeholder="Имя"  
                v-if="!login"
                class="form_input" 
                type="text" 
                v-model="user.name"/>
            <input placeholder="Фамилия"  
                v-if="!login"
                class="form_input" 
                type="text" 
                v-model="user.surname"/>
            <input placeholder="Отчество"  
                v-if="!login"
                class="form_input" 
                type="text" 
                v-model="user.patronymic"/>
            
            <button v-if="login" class="form_button">Войти</button>
            <button v-else class="form_button">Сохранить</button>
            <nuxt-link class="auth_msg" v-if="login" to="/auth/reg">Регистрация</nuxt-link>
            <nuxt-link class="auth_msg" v-else to="/auth" >Уже есть аккаунт?</nuxt-link>
        </div>
    </form>
</template>

<script>
export default {
    data(){
        return{
            user:{
                email:'',
                login:'',
                password:'',
                name: '',
                surname:'',
                patronymic:'',
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
        },
        onChange(event){
            this.user.photo = event.target.files[0]
            console.log(this.user.photo)
        },
        addChild(){
            this.user.childs.push('')
        }
    },
}
</script>