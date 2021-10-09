<template>
  <div class="top-4">

  </div>
</template>

<script>
export default {
  name: "Teacher",
  async mounted() {
    let data = await fetch("http://127.0.0.1:8000/api/course/");
    let res = await data.json();
    console.log(res)
  }
}
</script>

<style scoped>
.top-4 {
  margin-top: 4rem;
}
</style>
