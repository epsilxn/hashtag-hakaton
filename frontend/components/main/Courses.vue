<template>
    <div class="courses_container">
        <div class="courses">
            <div v-for="course in courses" :key="course.id" class="course_item">
                <div class="course_title">{{course.name}}</div>
                <div class="course_emoji">{{course.emoji}}</div>
                <div class="course_description">{{course.description}}</div>
                <div class="course_button">
                    <nuxt-link :to="'course/'+course.id">
                        <div class="btn">подробнее</div>
                    </nuxt-link>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    props:{
        courses:{
            type: Array,
            required: true
        }
    }
}
</script>