<template>
  <div>
    <div class="wrapper">
      <div class="username">
        {{ status.user.name }}
      </div>
      <div v-if="status.user.verified" class="ml">
        ✔
      </div>
      <div class="ml">
        @{{ status.user.screen_name }}
      </div>
      <div class="ml">
        • {{ timeDiff }}
      </div>
    </div>
  </div>
</template>

<script>
import moment from 'moment';

export default {
  name: 'TweetInfo',
  props: {
    status: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      timeDiff: null,
    };
  },
  methods: {
    calcTimeDiff() {
      const createdAt = moment(this.status.created_at);
      if (createdAt.isAfter(moment().subtract(1, 'days'))) this.timeDiff = createdAt.fromNow(true);
      else if (createdAt.isAfter(moment().startOf('year'))) this.timeDiff = createdAt.format('DD MMM');
      else this.timeDiff = createdAt.format('DD MMM, YYYY');
    },
  },
  computed: {
  },
  mounted() {
    this.calcTimeDiff();
    setInterval(this.calcTimeDiff, 5000);
  },
};
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  flex-direction: row;
}
.username {
  font-weight: 600;
}
.ml {
  margin-left: 5px;
}
</style>
