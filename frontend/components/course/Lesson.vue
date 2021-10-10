<template>
    <div class="lesson">
        <div class="lesson_count">
            {{idx}}
        </div>
        <div class="lesson_more">
            <div class="more_name">
                {{lesson.name}}
            </div>
            <div class="more_info">
                {{lesson.information}}
            </div>
            <div v-if="$store.getters.getStaff" @click="showModal" class="lesson_button">
                <div class="nbtn">
                    <div class="btn">Отметить</div>
                </div>
            </div>
        </div>
        <div class="more_time">
            <div class="date">
                Цена:
                <span class="red"> 
                  {{lesson.price}}р</span> &nbsp;
            </div>
            <div class="date">
                 
                     Длительность:<span class="red"> {{lesson.duration.slice(1, -3)}}ч &nbsp;
                     </span>
            </div>
            <div class="time">
                {{lesson.time.slice(0, -3) }} &nbsp;
            </div>
            <div class="date">
                 {{lesson.date}} &nbsp;
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        lesson:{
            type: Object,
            required: true
        },
        idx:{
            type: Number,
            default: 1
        }
    },
    methods:{
        showModal(){
            this.$emit('showModal')
        }
    }
}
</script>
