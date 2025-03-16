<template>
  <div
      class="fixed inset-0 flex items-center justify-center bg-gradient-to-b from-purple-600 to-blue-700 bg-opacity-75 z-50">
    <div class="w-16 h-16 border-4 border-t-transparent border-white rounded-full animate-spin"></div>
  </div>
</template>

<script setup>
import {onMounted} from 'vue'
import {useRouter} from 'vue-router'

const router = useRouter()


onMounted(async () => {
  window.Telegram.WebApp.ready()

  // Check if shared card
  const initData = window.Telegram.WebApp.initDataUnsafe
  const startParam = initData?.start_param

  if (startParam) {
    history.replaceState({}, document.title, window.location.pathname);
    return await router.push(`/user/${startParam}`)
  }

  // Get info from Telegram
  try {
    const userData = window.Telegram.WebApp.initDataUnsafe.user
    const tg_id = userData.id

    const response = await fetch(`https://thesortage.space/api/user/check`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
            tg_id: tg_id,
          }
      )
    })

    const responseData = await response.json()
    if (responseData.user.id) {
      return await router.push(`/user/${responseData.user.id}`)
    }
  } catch (error) {
  }

  // Redirect to the main page
  await router.push(`/create`)
})
</script>