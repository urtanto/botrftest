import { createRouter, createWebHistory } from 'vue-router'
import CreateCard from '@/components/CreateCard.vue'
import ViewCard from '@/components/ViewCard.vue'

const routes = [
  {
    path: '/',
    component: CreateCard
  },
  {
    path: '/user/:uuid',
    component: ViewCard
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router