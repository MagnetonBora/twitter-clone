<template>
  <div>
    <div class="wrapper">
      <div class="profile-image">
        <div v-if="user.profile_image">
          <img :src="user.profile_image" class="circle-border"/>
        </div>
        <div v-else>
          <div class="circle-border initials">
            {{ userInitials }}
          </div>
        </div>
      </div>
      <div class="input-box">
        <form @submit.prevent="sendStatus">
          <textarea placeholder="What's happening?" rows="1" v-model="text"
          @input="resizeTextarea" ref="textarea"></textarea>
          <div class="input-toolbox">
            <div>
              <i class="fa fa-image icon-item" aria-hidden="true"></i>
              <i class="fa fa-smile-o icon-item" aria-hidden="true"></i>
            </div>
            <input type="submit" class="btn" value="Tweet">
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import autosize from 'autosize';
import axios from 'axios';

export default {
  name: 'TweetInput',
  data() {
    return {
      text: '',
      user: this.$store.state.authUser,
    };
  },
  methods: {
    sendStatus() {
      axios.post(
        'http://127.0.0.1:8000/api/tweets/',
        {
          text: this.text,
          user: this.$store.state.authUser.id,
        },
        { headers: { Authorization: `Bearer ${this.$store.state.jwt}` } },
      )
        .then((res) => {
          console.log(res.data);
          this.$emit('add-status', res.data);
          this.text = '';
        })
        .catch((err) => {
          console.log(err);
        });
    },
    resizeTextarea() {
      autosize(this.$refs.textarea);
    },

  },
  computed: {
    userInitials() {
      return this.$store.state.authUser.name.match(/\b(\w)/g).join('');
    },
  },
};
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  margin: 15px 0;
  background-color: #fff;
  padding: 15px;
  border-radius: 15px;
  box-shadow: 0px 2px 2px 0px rgba(200,200,200,0.5);
}
textarea {
  border: none;
  font-size: 18px;
  font-weight: 400;
  margin: 10px 0;
  font-family: inherit;
  resize: none;
  width: 99%;
  outline: none;
  height: auto;
  overflow: none;
}
.circle-border {
  border-radius: 50%;
  width: 50px;
  height: 50px;
  min-width: 50px;
  min-height: 50px;
}
.initials {
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 20px;
  background-color: rgb(85, 168, 250);
}
.profile-image {
  margin: 0 15px 0 0;
}
.input-box {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.btn {
  border: none;
  padding: 10px 15px;
  background-color: rgb(85, 168, 250);
  border-radius: 20px;
  color: white;
  font-size: 14px;
  font-weight: 700;
}
.input-toolbox {
  display: flex;
  flex-direction: row;
  margin-top: 15px;
  justify-content: space-between;
}
.icon-item {
  padding: 10px;
  border-radius: 999px;
  transition: 0.3s;
}
.icon-item:hover {
  color: rgb(105, 193, 248);
  background-color: rgba(135, 206, 250, 0.3);
}
</style>
