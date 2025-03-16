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
        {{ selectedDay }}.{{ monthList.indexOf(selectedMonth) + 1 }}.{{ selectedYear }}
      </span>
    </div>

    <button
        @click="sendUserData"
        class="px-6 py-2 mt-6 font-semibold text-purple-700 bg-white rounded-full hover:bg-gray-100"
    >
      Продолжить
    </button>
  </div>
</template>

<script setup>
import {onMounted, ref} from 'vue'
import {useRouter} from 'vue-router'
import {VueScrollPicker} from 'vue-scroll-picker'
import "vue-scroll-picker/style.css";

const logs = ref('')
let data = {};

const router = useRouter()

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

  const initData = window.Telegram.WebApp.initDataUnsafe
  const startParam = initData?.start_param
  alert(startParam)
})


async function sendUserData() {
  try {
    window.Telegram.WebApp.ready()

    const userData = window.Telegram.WebApp.initDataUnsafe.user
    data.tg_id = userData.id
    data.first_name = userData.first_name ?? ""
    data.last_name = userData.last_name ?? ""
    data.username = userData.username
    data.birth_date = new Date(
        parseInt(selectedYear.value, 10),
        monthList.indexOf(selectedMonth.value),
        parseInt(selectedDay.value, 10) + 1,
    )

    const response = await fetch('https://thesortage.space/api/create_card', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data),
    })

    const responseData = await response.json()
    await router.push(`/user/${responseData.id}`)
  } catch (error) {
    alert(error);
  }
}
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