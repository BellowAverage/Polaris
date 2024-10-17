
--- 
title:  KubeSphere部署项目 
tags: []
categories: [] 

---
### KubeSphere部署简单项目demo
1. 参考官方文档： https://v2-1.docs.kubesphere.io/docs/zh-CN/quick-start/jenkinsfile-out-of-scm/， 以图形化方式构建流水线1. 在部署过程中，省略了 阶段三：代码质量分析 (Code Analysis)， 同时还省略了发送邮件的配置1. 在部署的过程中，是从gitee上拉取的项目，并把项目推送docker hub上（https://hub.docker.com/） 效果： <img src="https://img-blog.csdnimg.cn/7379c127184a4541a11af443f8913416.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d3b388ba1b2341e3a554c1946da4cd72.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/655df85c1a5a4be1a929acaf3d2061a4.png" alt="部署成功后，测试之">
### KubeSphere部署微服务项目

以一个test项目为例 参考官方文档： https://v2-1.docs.kubesphere.io/docs/zh-CN/quick-start/jenkinsfile-out-of-scm/， 以图形化方式构建流水线 在部署过程中，省略了 阶段三：代码质量分析 (Code Analysis)， 同时还省略了发送邮件的配置，和审核的功能。 参考上个项目的demo,进行微服务项目的部署 <img src="https://img-blog.csdnimg.cn/092a2d0d17344b27a5bc175ff8700437.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/01603e28d57d4f1aa14d3e0a28a0587a.png" alt="在这里插入图片描述"> 整个流水线 <img src="https://img-blog.csdnimg.cn/c7ac49e11e56482cb5578de2b19797e5.png" alt="在这里插入图片描述"> 部署成功后的服务
1. Jenkinsfile
```
pipeline {<!-- -->
  agent {<!-- -->
    node {<!-- -->
      label 'maven'
    }

  }
  stages {<!-- -->
    stage('拉取代码') {<!-- -->
      steps {<!-- -->
        git(url: 'https://gitee.com/qinenqi/gulimall.git', credentialsId: 'gitee-id', branch: 'master', changelog: true, poll: false)
      }
    }
    stage('构建并推送镜像') {<!-- -->
      steps {<!-- -->
        container('maven') {<!-- -->
          sh 'mvn -Dmaven.test.skip=true -gs `pwd`/mvn-settings.xml clean package'
          sh 'cd $APP_NAME &amp;&amp; docker build -f Dockerfile-online -t $REGISTRY/$DOCKERHUB_NAMESPACE/$APP_NAME:SNAPSHOT-$BUILD_NUMBER .'
          withCredentials([usernamePassword(credentialsId : 'dockerhub-id' ,passwordVariable : 'DOCKER_PASSWORD' ,usernameVariable : 'DOCKER_USERNAME' ,)]) {<!-- -->
            sh 'echo "$DOCKER_PASSWORD" | docker login $REGISTRY -u "$DOCKER_USERNAME" --password-stdin'
            sh 'docker push $REGISTRY/$DOCKERHUB_NAMESPACE/$APP_NAME:SNAPSHOT-$BUILD_NUMBER'
          }

        }

      }
    }
    stage('保存制品') {<!-- -->
      steps {<!-- -->
       archiveArtifacts '$APP_NAME/target/*.jar'
      }
    }
    stage('部署至 Dev 环境') {<!-- -->
     steps {<!-- -->
        kubernetesDeploy(enableConfigSubstitution: true, deleteResource: false, kubeconfigId: 'demo-kubeconfig', configs: "$APP_NAME/deploy/no-branch-dev/**")
      }
    }
  }
}

```

与上个项目相比，要时刻留意着 “ 
     
      
       
       
         A 
        
       
         P 
        
        
        
          P 
         
        
          N 
         
        
       
         A 
        
       
         M 
        
       
         E 
        
       
         ” 
        
       
         ， 
        
       
         有 
        
       
         关 
        
       
         的 
        
       
         路 
        
       
         径 
        
       
         ， 
        
       
         要 
        
       
         全 
        
       
         部 
        
       
         加 
        
       
         上 
        
       
      
        APP_NAME”，有关的路径，要全部加上 
       
      
    APPN​AME”，有关的路径，要全部加上APP_NAME。
