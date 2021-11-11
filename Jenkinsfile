properties([pipelineTriggers([pollSCM('* * * * *')])])
node{
    stage("clone"){
        git "https://github.com/lenats03/DevOps0909.git"
    }
    stage("show files"){
    bat "dir"    
    }
}
