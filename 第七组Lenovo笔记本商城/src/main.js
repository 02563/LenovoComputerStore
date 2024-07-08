/*
 * @Author: 吕 锐中 1286565437@qq.com
 * @Date: 2023-11-26 22:07:46
 * @LastEditors: 吕 锐中 1286565437@qq.com
 * @LastEditTime: 2023-12-31 23:53:51
 * @FilePath: \hello-world\src\main.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
import { createApp, h } from 'vue'
import router from './router'
import App from './App.vue'

createApp(App).mount('#app')
vue.use(router)

new Vue({
  render: h => h(App),
  router
})