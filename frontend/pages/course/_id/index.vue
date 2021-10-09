<template>
    <div class="page_container">
        <section class="course_view">
            <div class="view_header">
                <div class="view_emoji">😀</div>
                <div class="text_container">
                    <div class="container_header">{{course.name}}</div>
                    <div class="container_info">{{course.description}}</div>
                </div>
            </div>
            <div class="adding_info">
                <div class="hours"></div>
                <div class="adding info">
                    Преподаватель: <span class="violet">{{course.teacher}}</span>
                    <br/>
                    Количество часов: <span class="violet">10</span>
                </div>
            </div>
            <div class="lessons_container">
                <div v-if="[...course.lessons_in_course].length==0" class="form_message msg">Занятия ещё не добавлены</div>
                <Lesson v-for="(ls, index) in course.lessons_in_course" :key="ls.id" :idx="index+1" :lesson="ls"/>
            </div>
        </section>
    </div>
</template>

<script>
import axios from 'axios'
import Lesson from '@/components/course/Lesson'
export default {
    data(){
        return{
            course:{}
        }
    },
    mounted(){
        axios.get(`http://127.0.0.1:8000/api/course/${this.$route.params.id}/`).then((resp)=>{
            this.course = resp.data[0]
            console.log(this.course.lessons_in_course.length==0)
        });
    },
    components:{
        Lesson
    }
}
</script>