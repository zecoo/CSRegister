var app5 = new Vue({
  el: '#app-5',
  data: {
    message: 'Hello Vue.js!',
    stu_id: '',
    info: {
      name: '',
      id: '',
      department: '',
      school: '',
      major: '',
      home: '',
      experience: '',
      rewards: '',
      wishes: ''
    }
  },
  methods: {
    getMsg() {
      var _this = this;
      const path = 'http://127.0.0.1:5000/getMsg';
      axios.get(path).then(function(response){
        var msg = response.data.msg;
        _this.message = msg;
      }).catch(function(error){
        alert('Error ' + error);
      })
    },
    getSql() {
      console.log(this.stu_id);
      var _this = this;
      const path = 'http://127.0.0.1:5000/mysql/' + this.stu_id;
      console.log(path);
      axios.get(path).then(function(response){
        var result = response.data;
        console.log(result);
        _this.info.name = result.stu_name;
        _this.info.id = result.stu_id;
        _this.info.school = result.school;
        _this.info.major = result.major;
        _this.info.department = result.department;
        _this.info.home = result.home;
        _this.info.experience = result.experience;
        _this.info.rewards = result.rewards;
        _this.info.wishes = result.wishes;
        _this.message = result;
      }).catch(function(error){
        alert('Error ' + error);
      })
    }
  }
})