<template>
  <div>
    <div class="login_form">
      <input type="text"  class="qxs-ic_user qxs-icon"  placeholder="用户名" v-model="userName_re">
      <input type="text"  class="qxs-ic_email qxs-icon"  placeholder="邮箱" v-model="email_re">
      <input type="text"  class="qxs-ic_password1 qxs-icon"  placeholder="密码" v-model="password_re">
      <input type="text"  class="qxs-ic_password2 qxs-icon"  placeholder="确认密码" v-model="password_re2">
      <el-button class="login_btn" @click.native="register" type="primary" round :loading="isBtnLoading">注册</el-button>
    </div>
  </div>
</template>

<script>
import {getUsers, postUsers} from '../api/api.js'
 
  export default {
    data() {
      return {
        userName: '',
        password: '',
        userName_re: '',
        email_re:'',
        password_re: '',
        password_re2: '',
        isBtnLoading: false
      }
    },
    created () {
      if(JSON.parse( localStorage.getItem('user')) && JSON.parse( localStorage.getItem('user')).userName){
        this.userName = JSON.parse( localStorage.getItem('user')).userName;
        this.password = JSON.parse( localStorage.getItem('user')).password;
      }
    },
    computed: {
      btnText() {
        if (this.isBtnLoading) return '登录中...';
        return '登录';
      }
    },
    methods: {
      login() {
        if (!this.userName) {
          this.$message.error('请输入用户名');
          return;
        }
        if (!this.password) {
          this.$message.error('请输入密码');
          return;
        }
        getUsers().then(response => {
          var temp = response.data;
          var flag = 0;
          for (var i=0;i<temp.length;i++){
          if (temp[i].username == this.userName && temp[i].password == this.password){
            this.$message.error('登陆成功');
            flag = 1;
          }
          }
          if (flag==0){this.$message.error('用户不存在');}
        })
        
      },
      register(){
        if (!this.userName_re) {
          this.$message.error('请输入用户名');
          return;
        }
        if (this.email_re.indexOf("@sjtu.edu.cn") == -1) {
          this.$message.error('邮箱格式不正确');
          return;
        }
        if (!this.password_re) {
          this.$message.error('请输入密码');
          return;
        }
        if (!this.password_re2) {
          this.$message.error('请重新输入密码');
          return;
        }
        if (this.password_re ==this.password_re2){
          postUsers(this.userName_re,this.password_re,this.email_re).then(response => {
          console.log(response);
          this.userName_re = '';
          this.email_re = '';
          this.password_re = '';
          this.password_re2 = '';
          this.$message({
                message: '注册成功',
                type: 'success'
          });
          this.$router.push('/');
        })
        }
        else{
            this.$message.error('密码不一致');
          return;
          }
      }
    }
  }
</script>
<style>
  .outer_label {
    position: relative;
    left: 0;
    top: 0;
    width: 100%;
    height: 220px;
    background: -webkit-linear-gradient(left, #000099, #2154FA); /* Safari 5.1 - 6.0 */
    background: -o-linear-gradient(right, #000099, #2154FA); /* Opera 11.1 - 12.0 */
    background: -moz-linear-gradient(right, #000099, #2154FA); /* Firefox 3.6 - 15 */
    background: linear-gradient(to right, #000099 , #2154FA); /* 标准的语法 */
    /*background-color: #000099;*/
    text-align: center;
    filter: brightness(1.4);
  }
  .inner_label {
    position: absolute;
    left:0;
    right: 0;
    bottom: 0;
    top:0;
    margin: auto;
    height: 50px;
  }
  .qxs-icon {
    height: 40px;
    width: 90%;
    margin-bottom: 5px;
    padding-left: 10%;
    border: 0;
    border-bottom: solid 1px lavender;
  }
  .login_form {
    width: 30%;
    padding-top: 10%;
    padding-left: 35%;
    padding-right: 10%;
  }
  .qxs-ic_user {
    background: url("../assets/user.png") no-repeat;
    background-size: 13px 15px;
    background-position: 3%;
  }
  .qxs-ic_email {
    background: url("../assets/email.png") no-repeat;
    background-size: 13px 15px;
    background-position: 3%;
  }
  .qxs-ic_password1 {
    background: url("../assets/key.png") no-repeat;
    background-size: 13px 15px;
    background-position: 3%;
  }
  .qxs-ic_password2 {
    background: url("../assets/key.png") no-repeat;
    background-size: 13px 15px;
    background-position: 3%;
    margin-bottom: 20px;
  }
  .login_logo {
    height: 100%;
  }
  .login_btn {
    width: 50%;
    font-size: 16px;
    background: -webkit-linear-gradient(left, #000099, #2154FA); /* Safari 5.1 - 6.0 */
    background: -o-linear-gradient(right, #000099, #2154FA); /* Opera 11.1 - 12.0 */
    background: -moz-linear-gradient(right, #000099, #2154FA); /* Firefox 3.6 - 15 */
    background: linear-gradient(to right, #000099 , #2154FA); /* 标准的语法 */
    filter: brightness(1.4);
  }
</style>
