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
            <input placeholder="Ваши ФИО"  
                v-if="!login"
                class="form_input" 
                type="text" 
                name="FIO" 
                id="FIO"
                v-model="user.fio"/>
            <div v-if="!login" class="input__wrapper">
                <input placeholder="Фото"  
                    v-if="!login"
                    type="file" 
                    name="photo" 
                    id="photo"
                    class="input input__file"
                    @change="onChange"/>
                <label for="photo" class="input__file-button">
                    <span class="input__file-icon-wrapper">
                        <span class="material-icons">
                            cloud_upload
                        </span>
                    </span>    
                    <span class="input__file-button-text">Выберите файл</span>
                </label>
            </div>
            <div v-if="!login" class="child_container">
                <input v-for="(child,index) in user.childs" :key="index" placeholder="Ребёнок"  
                    class="form_input" 
                    type="text" 
                    name="child" 
                    id="child"
                    v-model="user.childs[index]"/>
                <span @click="addChild" class="plus material-icons">
                    add_circle_outline
                </span>
            </div>
            
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
                password:'',
                fio: '',
                photo:'',
                childs:[''],
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