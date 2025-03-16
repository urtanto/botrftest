<template>
  <div
      class="flex flex-col items-center justify-center min-h-screen px-4 py-8 text-white bg-gradient-to-b from-purple-600 to-blue-700">
    <div class="mb-6 text-center">
      <h1 class="mt-1 text-2xl font-bold">Введи свою дату рождения</h1>
    </div>

    <div class="relative flex items-center space-x-6">
      <VueScrollPicker
          v-model="selectedDay"
          :options="dayList"
          class="scroll-picker"
      />

      <VueScrollPicker
          v-model="selectedMonth"
          :options="monthList"
          class="w-24"
      />

      <VueScrollPicker
          v-model="selectedYear"
          :options="yearList"
          class="scroll-picker"
      />

    </div>

    <div class="mt-6 text-lg">
      Выбранная дата:
      <span class="font-semibold">
        {{ selectedDay }}.{{ monthList.indexOf(selectedMonth) }}.{{ selectedYear }}
      </span>
    </div>
    <p>logs: {{ logs }}</p>

    <button
        class="px-6 py-2 mt-6 font-semibold text-purple-700 bg-white rounded-full hover:bg-gray-100"
    >
      Продолжить
    </button>
  </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import {VueScrollPicker} from 'vue-scroll-picker'
import "vue-scroll-picker/style.css";

const logs = ref('')
let data = {};

const dayList = Array.from({length: 31}, (_, i) => (i + 1).toString().padStart(2, '0'))
const monthList = [
  'Январь', 'Февраль', 'Март', 'Апрель',
  'Май', 'Июнь', 'Июль', 'Август',
  'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
]
const yearList = Array.from({length: 2025 - 1925 + 1}, (_, i) => (1925 + i).toString()).reverse()

const selectedDay = ref(dayList[0])
const selectedMonth = ref(monthList[0])
const selectedYear = ref(yearList[0])

onMounted(() => {
  window.Telegram.WebApp.ready()

  const userData = window.Telegram.WebApp.initDataUnsafe.user
  data.tg_id = userData.id
  data.first_name = userData?.first_name
  data.last_name = userData?.last_name
  data.username = userData.username
  // data.birth_date = new Date(
      // parseInt(selectedDay, 10),
      // monthList.indexOf(selectedMonth),
      // parseInt(dayNum, 10)
  // )

  // logs.value = JSON.stringify(data)
  logs.value = JSON.stringify(
      {
        day: parseInt(selectedDay.value),
        month: monthList.indexOf(selectedMonth),
        year: parseInt(selectedYear.value)
      }
  )
})
</script>

<style>
.scroll-picker {
  width: 100px;
}

.vue-scroll-picker-layer-top {
  background: none;
}

.vue-scroll-picker-item[aria-selected=true] {
  color: white;
}

.vue-scroll-picker-layer-bottom {
  background: none;
}
</style>