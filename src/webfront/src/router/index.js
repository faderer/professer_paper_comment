import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import about from '@/components/about'
import teacher from '@/components/teacher'
import register from '@/components/register'
import login from '@/components/login'
import xingchaoping from '@/components/xingchaoping'
import gudawu from '@/components/gudawu'
import shengliliu from '@/components/shengliliu'
import xinghaojiang from '@/components/xinghaojiang'
import chenyuan from '@/components/chenyuan'
import lijianhua from '@/components/lijianhua'
import lishenghong from '@/components/lishenghong'
import shaoshuo from '@/components/shaoshuo'
import tangdeng from '@/components/tangdeng'
import hanshuai from '@/components/hanshuai'
import liushengyun from '@/components/liushengyun'
import wanglei from '@/components/wanglei'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/about',
      component: about
    },
    {
      path: '/teacher',
      component: teacher
    },
    {
      path: '/register',
      component: register
    },
    {
      path: '/login',
      component: login
    },
    {
      path: '/xingchaoping',
      component: xingchaoping
    },
    {
      path: '/gudawu',
      component: gudawu
    },
    {
      path: '/shengliliu',
      component: shengliliu
    },
    {
      path: '/xinghaojiang',
      component: xinghaojiang
    },
    {
      path: '/chenyuan',
      component: chenyuan
    },
    {
      path: '/lijianhua',
      component: lijianhua
    },
    {
      path: '/lishenghong',
      component: lishenghong
    },
    {
      path: '/shaoshuo',
      component: shaoshuo
    },
    {
      path: '/tangdeng',
      component: tangdeng
    },
    {
      path: '/hanshuai',
      component: hanshuai
    },
    {
      path: '/liushengyun',
      component: liushengyun
    },
    {
      path: '/wanglei',
      component: wanglei
    }
  ]
})
