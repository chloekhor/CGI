module.exports = {
  parser: 'vue-eslint-parser', // 使用 vue-eslint-parser 解析 .vue 文件
  parserOptions: {
    parser: '@babel/eslint-parser',  // 使用 Babel 解析 JavaScript 语法
    ecmaVersion: 2020,               // 支持 ECMAScript 2020 语法
    sourceType: 'module',            // 支持 ECMAScript 模块
  },
  extends: [
    'eslint:recommended',
    'plugin:vue/vue3-essential',     // Vue 3 的必要规则集
  ],
  rules: {
    'vue/multi-word-component-names': 'off',  // 关闭 Vue 组件名称多单词检查
  },
};
