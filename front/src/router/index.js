import { createRouter, createWebHistory } from 'vue-router'
import CreateCard from '@/components/CreateCard.vue'
import SecondPage from '@/components/ViewCard.vue'

const routes = [
  {
    path: '/',
    component: CreateCard
  },
  {
    path: '/user/:uuid',
    component: SecondPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router