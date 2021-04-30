<template>
    <div>
      <div class="Faculty">
          <h1>
            教师简介
          </h1>
          <ul>

                        <router-link to="/shaoshuo" class="tap">
                        
                   			<img src="https://infosec.sjtu.edu.cn/Management/Upload/[XY_JiaoShiMingLu]faaf20088bb649c6a860777d1d35292f/202122516015738qwCex.png">
                            
							<h2>邵硕</h2>
								<h5>职称：长聘教轨副教授</h5>
							<p>研究兴趣：<p>
	<span style="color:#666666;font-family:sans-serif;font-size:14px;font-style:normal;font-weight:400;"><span style="color:#666666;font-family:sans-serif;font-size:14px;font-style:normal;font-weight:400;"><br />
&nbsp;&nbsp;</span></span> 
							<p>邮箱：shuoshao@sjtu.edu.cn</p>
							<div class="cb"></div>
                   		</router-link>

				</ul>
      </div>
      <div class="paper">
        <h1>
          论文发表情况
        </h1>
        <span>
          <p1>标题</p1><p2>引用次数</p2><p3>年份</p3>
        </span>
        <span1 
          v-for="(i,index) in papers"
          :key="index"
        >
          <p1><p4 @click="downloadpdf(i)">{{i.title}}</p4><p5>{{i.subtitle}}</p5></p1><p2>{{i.citation}}</p2><p3>{{i.pub_date}}</p3>
        </span1>
      </div>
      <div class="comment">
        <h1>
          学生评价
        </h1>
        <span1 
          v-for="(i,index) in comments"
          :key="index"
        >
          <p1>{{i.content}}</p1><p3>{{i.pub_date}}</p3>
        </span1>
        <form action="" class="commentinput" v-if="this.GLOBAL.iflog==1">
          输入评价：<input type="text" placeholder="评价" v-model="inputcontent" ><br>
        </form>
        <button type="submit" @click="submitComments()" v-if="this.GLOBAL.iflog==1">submit</button>
      </div>
    </div>
</template>


<script>
import {getPapers, postPapers, getComments, postComments} from '../api/api.js'
export default {
  data() {
    return {
      teacher:"Shuo Shao",
      papers:[

      ],
      comments:[

      ]
    };
  },
  methods: {
    loadPapers () {
      getPapers().then(response => {
        var temp = response.data;
        this.papers = [];
        for (var i = 0;i < temp.length;i++){
          if (temp[i].author == this.teacher)
            this.papers.push(temp[i])
        }
      })
    }, // load books list when visit the page
    // bookSubmit () {
    //   postBook(this.inputBook.name, this.inputBook.author).then(response => {
    //     console.log(response)
    //     this.loadBooks()
    //   })
    // } // add a book to backend when click the button
    addpaper () {
      var temp = {
        title:'Coding theory: a first course',
        subtitle:'Cambridge University Press',
        citation:363,
        pub_date:2004,
      }
      this.papers.push(temp);
    },
    loadComments () {
      getComments().then(response => {
        var temp = response.data;
        this.comments = [];
        for (var i = 0;i < temp.length;i++){
          if (temp[i].teacher == this.teacher)
            this.comments.push(temp[i])
        }
      })
    },
    submitComments () {
      postComments(this.teacher,this.inputcontent,this.dateFormat("YYYY-mm-dd HH:MM:SS", new Date())).then(response => {
        this.inputcontent = ''
        console.log(response)
        this.loadComments()
      })
    },
    dateFormat(fmt, date) {
    let ret;
    const opt = {
        "Y+": date.getFullYear().toString(),        // 年
        "m+": (date.getMonth() + 1).toString(),     // 月
        "d+": date.getDate().toString(),            // 日
        "H+": date.getHours().toString(),           // 时
        "M+": date.getMinutes().toString(),         // 分
        "S+": date.getSeconds().toString()          // 秒
        // 有其他格式化字符需求可以继续添加，必须转化成字符串
    };
    for (let k in opt) {
        ret = new RegExp("(" + k + ")").exec(fmt);
        if (ret) {
            fmt = fmt.replace(ret[1], (ret[1].length == 1) ? (opt[k]) : (opt[k].padStart(ret[1].length, "0")))
        };
    };
    return fmt;
    },
    downloadpdf: function(i){
      if (i.filename != ''){
        var value = "http://localhost:8000/paper/test/"+this.teacher+"/"+i.subtitle+"/"+i.filename;
        value.replace(/\s+/g,"%20");
        window.location.href = value;
      }
      else{this.$message.error('暂无pdf');}
    }
  
  },
  created: function () {
    this.loadPapers()
    this.loadComments()
  }
};
</script>

<style lang="scss" scoped>
.Faculty {border-bottom:#e5e5e5 1px dashed;padding:0px 0px 14px 0px;}
.Faculty h1{text-align: left;font-size: 20px;}
.Faculty h3 {font-size:14px; font-weight: 700; padding-left: 10px; line-height:30px;}
.Faculty li {float:left; width: 330px; background: #f8f8f8; margin: 10px; line-height: 20px; padding-right: 10px;}
.Faculty a {text-decoration: none;}
.Faculty > ul > li > a > img {width: 130px; float: left; margin-right: 10px;}
.Faculty img {width: 130px; height: 168px;}
.Faculty h2 {font-size: 16px; font-weight: 700; color: #840f0f; padding-top: 5px;line-height:10px;}
.Faculty h5 {font-size:14px; font-weight: 700; padding: 0px 0px;line-height:20px;}
.Faculty h4 {color: #fff; font-size: 14px; font-weight: 700; line-height: 30px; background: #840f0f; margin: 20px 0px; padding: 0px 10px;}
.Faculty p {color: #666;font-size: 10px;line-height: 15px;}
.cb {clear:both}
.paper {justify-content: center;}
.paper h1{text-align: left;font-size: 20px;}
.paper span{display: flex;margin-top: 10px;background-color: rgb(248, 241, 241);}
.paper span1{display: flex;margin-top: 50px;}
.paper p1{position: absolute;left: 30px;color: #2d64ca;}
.paper p2{position: absolute;left: 700px;}
.paper p3{position: absolute;left: 800px;}
.paper p4{display: block;color: #2d64ca;font-size: 14px;}
.paper p5{display: block;color: #afacac;font-size: 12px;text-align: left;margin-top: 5px;}
.comment {border-top:#e5e5e5 1px dashed;padding:0px 0px 14px 0px;margin-top: 40px;}
.comment h1{text-align: left;font-size: 20px;}
.comment span1{display:flex; margin-top: 40px;}
.comment p1{position: absolute;left: 30px;color: #2a2b2c;font-size: 14px;}
.comment p3{position: absolute;left: 750px;font-size: 10px;color: #797c7e;}
.commentinput {margin-top: 50px;}
</style>