import Vue from 'vue'
//对应你要跳转的组件
import HelloWorld from "../components/HelloWorld"; 
import Router from 'vue-router'

Vue.use(Router)
export default new Router({
    routes: [
        {path:'component/login.html',
        name:'hello',
        component:HelloWorld}
    ]
})
