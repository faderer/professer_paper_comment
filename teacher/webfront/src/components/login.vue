<template>
    <div>
        <!-- <div class="outer_label">
        <img class="inner_label login_logo" src="../assets/logo.png">
        </div> -->

        <div class="login_form">
            <input type="text"  class="qxs-ic_user qxs-icon"  placeholder="用户名" v-model="userName">
            <input type="text"  class="qxs-ic_password2 qxs-icon"  placeholder="密码" v-model="password">
            <el-button class="login_btn" @click.native="login" type="primary" round :loading="isBtnLoading">登录</el-button>
            <div style="margin-top: 10px">
                <span style="float: right;color: #A9A9AB; font-size:10px">忘记密码？</span>
            </div>
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
            this.$message({
                message: '登陆成功',
                type: 'success'
            });
            flag = 1;
            this.$root.iflog = 1;
            this.$router.push('/');
          }
          }
          if (flag==0){this.$message.error('用户不存在');}
        })
        
      },
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
    