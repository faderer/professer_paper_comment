<template>
  <div id="app">
    <div class="overall">
    <div class="top">
      <div class="tab-box">
      <span
        v-for="(i,index) in tabs"
        :key="index"
        :class="defaultIndex==index?'active':''"
        @click="defaultIndex=index"
      >
        <div class="dot"></div>
        <router-link :to="i.url" tag="span">
          {{i.text}}
        </router-link>
      </span>
      <div class="bar-box">
        <div class="bar"></div>
      </div>
      </div>
      <div class="tab-box2">
        <span v-if="this.GLOBAL.iflog==0" class="defaultIndex==index?'active':''">
        <div class="dot"></div>
        <router-link to="/register" tag="span">
          sign up
        </router-link>
        </span>
        <span v-if="this.GLOBAL.iflog==1" class="defaultIndex==index?'active':''" @click="logout">
        <div class="dot"></div>
        <router-link to="/" tag="span">
          sign out
        </router-link>
        </span>
      </div>
    </div>


    <svg style="width: 0; height: 0;">
      <defs>
        <filter id="goo">
          <feGaussianBlur in="SourceGraphic" result="blur" stdDeviation="4" />
          <feColorMatrix
            in="blur"
            mode="matrix"
            values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -7"
            result="goo"
          />
          <feBlend in2="goo" in="SourceGraphic" result="mix" />
        </filter>
      </defs>
    </svg>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      thatnum: 0,
      defaultIndex: 0,
      tabs:[
        {
          text:'Home',
          url:'/'
        },
        {
          text:'About',
          url:'/about'
        },
        {
          text:'Teacher',
          url:'/teacher'
        }
      ]

    };
  },
  mounted(){
    this.thatnum=this.tabName
  },
  methods: {
    addClassName: function(index) {
      this.thatnum = index;
    },
    logout(){
      this.GLOBAL.iflog = 0;
      this.$router.go(0);
    }
  }
}
</script>

<style lang="scss" scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  display: normal;
  justify-content: center;
  align-items: normal;
  // background-image: url('./assets/u.jpg');
  background-size: 100% 100%;
  height: 100%;
  background-size: cover;
}
.navi{
  display: flex;
  text-align: left;
  background-image: url('./assets/b.jpg');
  background-size: cover;
  margin-top: 0%;
  margin-bottom: 0%;
  line-height: 0%;
  text-decoration: none;

}
.tap{
  margin-top: 0%;
  margin-bottom: 0%;
  line-height: 50%;
  margin-inline: 30px;
}
.a{
  text-decoration: none;
}
p{
  margin-top: 0%;
  margin-bottom: 0%;
  color: #cccccc;
  font-size: 14px;
  margin-inline: 30px;
  text-decoration: none;
}
.router-link{
  text-decoration: none;
}
.active p{
  color: #1296DB;
  text-decoration: none;
}

.top{
  display: flex;
}


.tab-box {
  box-shadow: 0 0 5px #ccc;
  width: 400px;
  height: 50px;
  background: #0084ff;
  border-radius: 2px;
  display: flex;
  position: relative;
  z-index: 99;
}

.tab-box2 {
  box-shadow: 0 0 5px #ccc;
  width: 100px;
  height: 50px;
  background: #0084ff;
  border-radius: 5px;
  display: flex;
  margin-left: 400px;
}
//------------------------------------鼠标点击后加载类似水滴的动画部分-------------------------------------
.tab-box span {
  display: block;
  flex-grow: 1;
  line-height: 50px;
  font-weight: bold;
  cursor: pointer;
  position: relative;
  transition: 0.5s ease;
  user-select: none;
  color: white;
  border-bottom: 3px solid transparent;
  .dot {
    display: inline-block;
    width: 30px;
    height: 10px;
    //此处引用的是滤镜效果，相当于在字母的最上层放置一个滤镜模板，在这个模板里小圆球的移动，会有种黏黏的感觉
    -webkit-filter: url("#goo");
    filter: url("#goo");
    position: absolute;
    background: #0084ff;
    left: calc(50% - 15px);
    top: 1px;
    &::after {
      content: "";
      position: absolute;
      left: calc(50% - 6px);
      width: 12px;
      height: 12px;
      display: block;
      background: #0084ff;
      border-radius: 50%;
     
    }
  }
}
.tab-box2 span {
  display: block;
  flex-grow: 1;
  line-height: 50px;
  font-weight: bold;
  cursor: pointer;
  position: relative;
  transition: 0.5s ease;
  user-select: none;
  color: white;
  border-bottom: 3px solid transparent;
  .dot {
    display: inline-block;
    width: 30px;
    height: 10px;
    //此处引用的是滤镜效果，相当于在字母的最上层放置一个滤镜模板，在这个模板里小圆球的移动，会有种黏黏的感觉
    -webkit-filter: url("#goo");
    filter: url("#goo");
    position: absolute;
    background: #0084ff;
    left: calc(50% - 15px);
    top: 1px;
    &::after {
      content: "";
      position: absolute;
      left: calc(50% - 6px);
      width: 12px;
      height: 12px;
      display: block;
      background: #0084ff;
      border-radius: 50%;
     
    }
  }
}
.active {
  text-shadow: 0 0 10px white;
  border-bottom: 3px solid white !important;
}
.active .dot::after {
  animation: gooey 1s both 1 ease;
}
@keyframes gooey {
  50% {
    transform: translateY(-30px) scaleX(0.8);
  }
}
//------------------------------------鼠标点击后加载类似水滴的动画部分-------------------------------------



//------------------------------------鼠标经过的下划线跟随部分-------------------------------------
.tab-box span:hover {
  text-shadow: 0 0 10px white;
}

.tab-box span:nth-of-type(1):hover + * + * + .bar-box .bar {
  left: 0;
}
.tab-box span:nth-of-type(2):hover + * + .bar-box .bar {
  left: 33.3333%;
}
.tab-box span:nth-of-type(3):hover + .bar-box .bar {
  left: 66.6666%;
}
.bar-box {
  width: 100%;
  height: 100%;
  border-radius: 2px;
  overflow: hidden;
  position: absolute;
  z-index: -1;
}
.tab-box .bar {
  width: 33.3333%;
  height: 3px;
  position: absolute;
  left: -33.3333%;
  bottom: 0;
  background: white;
  transition: 0.5s ease;
  opacity: 0.9;
}
//------------------------------------鼠标经过的下划线跟随部分-------------------------------------

</style>
