const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

module.exports = {
  devServer: {
    host: "0.0.0.0",
    port: 8081,
    https: false, // ❌ 不要让 Vue.js 自己启用 HTTPS
    allowedHosts: "all",
    proxy: {
      "/api": {
        target: "https://localhost",
        changeOrigin: true,
        secure: false, // 让 Vue.js 信任 Nginx 的 HTTPS
      },
    },
  },
};




//module.exports = {
// devServer: {
//    https: true, // 让 Vue.js 继续用 HTTP 运行（Nginx 负责 HTTPS）
//    //host: "0.0.0.0",  // 让 Vue.js 监听所有 IP（包括 `localhost` 和 `192.168.1.21`）
//    //allowedHosts: "all",  // 允许任何主机访问
//    key: "C:/nginx/ssl/localhost.key",
//    cert: "C:/nginx/ssl/localhost.crt",
//    port: 8081,   // 确保 Vue.js 启动时使用 8081 端口
//    proxy: {
//      "/api": {
//        target: "https://localhost",  // 确保代理目标是 HTTPS
//        secure: false,  // 防止证书验证
//      },
//    },
//  },
//};
