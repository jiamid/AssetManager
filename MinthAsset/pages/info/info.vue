<template>
	<view>
		<view class="uni-list" style="text-align: center;width: 750upx;">
			<view class="uni-list-cell">资产编号:{{Asset.assetNum}}</view>
			<view class="uni-list-cell">资产名称:{{Asset.assetName}}</view>
			<view class="uni-list-cell">用户名称:{{Asset.userName}}</view>
			<view class="uni-list-cell">用户工号:{{Asset.empId}}</view>
			<input class="uni-input" v-model="userName" type="text" placeholder="在此输入新使用人" value='hello'/>
			<view class="uni-list-cell">资产归属:{{Asset.ownerDept}}</view>
			<view class="uni-list-cell">管理账号:{{Asset.adminId}}</view>
			<view class="uni-list-cell">备注:{{Asset.tagText}}</view>
			<view class="uni-list-cell">最后修改时间:{{Asset.lastTime}}</view>
		<button  @click="checkThis()" style="width: 750upx;">点检</button>
		<button  @click="updataUser()" style="width: 750upx;">更新使用人</button>
		<button  @click="backIndex()" style="width: 750upx;">返回主页</button>
		<button  @click="delThis()" style="width: 750upx;">删除该页</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				Asset : [],
				userName:"",
				hostAd:"http://10.8.40.218",
			}
		},
		onLoad:function(e){
			// console.log(e.assetNum);
			uni.showLoading({
				title:"加载中...."
			})
			uni.request({
				url: this.hostAd +'/api/v1/Asset/?assetNum='+e.assetNum,
				method: 'GET',
				data: {},
				success: res => {
					
					this.Asset = res.data.data[0];
					uni.hideLoading();
				},
				fail: () => {},
				complete: () => {}
			});
		},
		methods: {
			backIndex:function(){
				uni.redirectTo({
					url: '../index/index',
				});
			},
			delThis:function () {
				uni.request({
					  	    url: this.hostAd +'/api/v1/Asset/',
							data: {'assetNum':this.Asset.assetNum},
					  		dataType: 'json',
					  		method: 'DELETE',
					  	    header: {
					  	        'custom-header': 'delete',
					  			'content-type': 'application/json'
					  	    },
					
					success: res => {
						uni.redirectTo({
							url: '../index/index'
						});
					},
					fail: (e) => {
					},
					complete: () => {}
				});
			},
			checkThis:function () {
				uni.request({
					url: this.hostAd +'/api/v1/Asset/',
					method: 'PUT',
					data: {
						'assetNum':this.Asset.assetNum,
						'assetName':this.Asset.assetName,
						'empId':this.Asset.empId,
						'userName':this.Asset.userName,
						'ownerDept':this.Asset.ownerDept,
						'adminId':this.Asset.adminId,
						'tagText':'已检查ok',
					},
					header: {
					        'content-type': "application/json",
					},
					success: res => {
						uni.redirectTo({
							url: '../info/info?assetNum='+this.Asset.assetNum
						});
					},
					fail: (e) => {
					},
					complete: () => {}
				});
			},
			updataUser:function() {
				uni.request({
					url: this.hostAd +'/api/v1/Asset/',
					method: 'PUT',
					data: {
						'assetNum':this.Asset.assetNum,
						'assetName':this.Asset.assetName,
						'empId':this.Asset.empId,
						'userName':this.userName,
						'ownerDept':this.Asset.ownerDept,
						'adminId':this.Asset.adminId,
						'tagText':'已检查',
					},
					header: {
					        'content-type': "application/json",
					},
					success: res => {
						uni.redirectTo({
							url: '../info/info?assetNum='+this.Asset.assetNum
						});
					},
					fail: (e) => {
					},
					complete: () => {}
				});
			}
		},
		
	}
</script>

<style>

</style>
