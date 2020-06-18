<template>
	<view class="content" style="text-align: center;">
			<view class="uni-list" style="align-items: center;width: 750upx">
				<view class="uni-list-cell-navigate uni " >
					<button type="primary" @click="tel()" style="width: 750upx;">扫描二维码</button>
				</view>
				<view class="uni-list-cell-navigate uni " >
					<input class="uni-input" v-model="assetNum" type="text" placeholder="在此输入需访问资产编号" style="width: 600upx;"/>
					<button type="primary" @click="goinfo()" style="width: 150upx;">Go</button>
				</view>
				<view class="uni-list-cell-navigate uni " >
					<button type="primary" @click="goadd()" style="width: 750upx;">添加新资产</button>
				</view>
				<view class="uni-list-cell-navigate uni " >
					<a href='http://10.8.40.218/api/v1/getAsset/'  class="Adown">下载资产信息表格</a>
				</view>
						<view class="uni-list-cell" hover-class="uni-list-cell-hover" v-for="(item,index) in Assets" :key="index" @tap="openinfo" :data-assid="item.assetNum">
							<view class="uni-list-cell-navigate uni uni-navigate-right" style="width: 750upx;">
								{{item.assetNum}}:{{item.userName}}
							</view>
						</view>
			</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				Assets : [],
				hostAd :'http://10.8.40.218',
				assetNum : '',
			};
		},
		onLoad:function(){
			uni.showLoading({
				title:"加载中...."
			})
			uni.request({
				url: this.hostAd + '/api/v1/Asset/',
				method: 'GET',
				data: {},
				success: res => {
					this.Assets = res.data.data;					
					uni.hideLoading();
				},
				fail: () => {},
				complete: () => {}
			});
		},
		onBackPress:function(){
			uni.showLoading({
				title:"加载中...."
			})
			uni.request({
				url: this.hostAd +'/api/v1/Asset/',
				method: 'GET',
				data: {},
				success: res => {
					this.Assets = res.data.data;					
					uni.hideLoading();
				},
				fail: () => {},
				complete: () => {}
			});
		},
		
		methods: {
			openinfo(e) {
				var id = e.currentTarget.dataset.assid;
				uni.navigateTo({
					url: '../info/info?assetNum='+id
				});
			},
			tel:function () {
				uni.scanCode({
					success:function(res){
						var Qcode = JSON.stringify(res.result).slice(1,-1);
						console.log(Qcode);
						var id = Qcode;
						uni.navigateTo({
							url: '../info/info?assetNum='+id
						});
						
					}
				})
			},
			goinfo:function() {
				uni.navigateTo({
					url: '../info/info?assetNum='+ this.assetNum
				});
			},
			goadd:function() {
				uni.navigateTo({
					url: '../addOne/addOne'
				});
			},
			getExcel:function(){
				uni.downloadFile({
					url: this.hostAd+'/api/v1/getAsset/'
				});
				
			}
		},
	}
</script>

<style>
	.Adown{
		text-decoration: none;
		width: 750upx;
		height: auto;
		border: 1px solid #4CD964;
		background: #4CD964;
		border-radius: 10px;
		color: #FFFFFF;
	}
	.Adown:hover{
		border: 1px solid #4CD964;
		background:#DD524D;
		color: #333333;
	}
</style>
