<template>
  <div class="page_container">
    <div class="main_page">
      <div class="main_info">
        <p class="hello">Здравствуйте, родитель</p>
        <div class="line"></div>
        <div class="flex_info">
            <div class="parent_info">
              <p>Фамилия: Алиев</p>
              <p>Имя: Давид</p>
              <p>Отчество: Мурадович</p>
            </div>
            <div class="child_info">
              <div class="child_one">
                <p>Ваш ребенок: Умывалкин Максим Александрович</p>
                <p>Записан на курс: Робототехника</p>
              </div>
              <div class="child_two">
                <p>Ваш ребенок: Изис Александр Валерьевич</p>
                <p>Записан на курс: Основы программирования</p>
              </div>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Parent from "@/components/lk/Parent"
export default {
  name: "parent",
  data() {
    return{
      loh:123
    }
  },
  components: {
    Parent
  },
  async mounted() {
  let data = await fetch("http://127.0.0.1:8000/api/parent");
  let res = await data.json();
  console.log(res)
  }
}
</script>

<style scoped>

</style>
