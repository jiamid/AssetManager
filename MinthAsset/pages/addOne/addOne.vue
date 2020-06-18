<template>
	<view>
		<view class="uni-list" style="text-align: center;width: 750upx;">
			<view class="uni-list-cell">资产编号:
				<input class="uni-input" v-model="assetNum" type="text" placeholder="在此输入资产编号" style="width: 500upx;"/>
			</view>
			<view class="uni-list-cell">资产名称:
				<input class="uni-input" v-model="assetName" type="text" placeholder="在此输入资产名称" style="width: 500upx;"/>
			</view>
			<view class="uni-list-cell">用户名称:
				<input class="uni-input" v-model="userName" type="text" placeholder="在此输入用户名称" style="width: 500upx;"/>
			</view>
			<view class="uni-list-cell">用户工号:
				<input class="uni-input" v-model="empId" type="text" placeholder="在此输入用户工号" style="width: 500upx;"/>
			</view>
			<view class="uni-list-cell">资产归属:
				<input class="uni-input" v-model="ownerDept" type="text" placeholder="在此输入资产归属" style="width: 500upx;"/>
			</view>
			<view class="uni-list-cell">备注:
				<input class="uni-input" v-model="tagText" type="text" placeholder="在此输入备注信息" style="width: 500upx;"/>
			</view>
			<button  @click="addPage()" style="width: 750upx;">提交</button>
		</view>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				hostAd:'http://10.8.40.218',
				assetNum:'',
				assetName:'',
				userName:'',
				empId:'',
				ownerDept:'',
				tagText:'',
				adminId:'admin',
				
			}
		},
		methods: {
			addPage:function () {
				uni.request({
					url: this.hostAd +'/api/v1/Asset/',
					method: 'POST',
					data: {
						'assetNum':this.assetNum,
						'assetName':this.assetName,
						'empId':this.empId,
						'userName':this.userName,
						'ownerDept':this.ownerDept,
						'adminId':this.adminId,
						'tagText':this.tagText,
					},
					header: {
					        'content-type': "application/json",
					},
					success: res => {
						uni.redirectTo({
							url: '../info/info?assetNum='+this.assetNum
						});
					},
					fail: (e) => {
					},
					complete: () => {}
				});
			},
		}
	}
</script>

<style>

</style>
