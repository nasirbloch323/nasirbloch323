<div align="center">

<!-- HEADER -->
<img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=0:0D1117,100:00F0FF&text=NASIR%20MEHMOOD&fontColor=fff&fontSize=55&desc=DevOps%20Engineer%20%7C%20Cloud%20%26%20Automation%20Specialist&descSize=18&descAlignY=75" />

<br>

<!-- TYPING ANIMATION -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=1000&color=00F0FF&center=true&vCenter=true&width=800&lines=AWS+%7C+Docker+%7C+Kubernetes+%7C+Terraform;CI%2FCD+%7C+Jenkins+%7C+ArgoCD+%7C+Helm;IaC+%7C+Ansible+%7C+GitOps+%7C+SRE" />

<br><br>

<!-- VIEWS & FOLLOWERS -->
<img src="https://komarev.com/ghpvc/?username=nasirbloch323&label=Profile%20Views&color=0e75b6&style=for-the-badge" />
<img src="https://img.shields.io/github/followers/nasirbloch323?label=Followers&style=for-the-badge&color=0e75b6&logo=github" />

</div>

---

<!-- DEVOPS TERMINAL -->
<div align="center">
  <h2>🚀 DevOps Environment in Action</h2>
</div>

```bash
nasir@devops:~$ kubectl get pods -n production
NAME                          READY   STATUS    RESTARTS   AGE
flask-app-7c4b9f5d8-x2v4p    1/1     Running   0          5d
mysql-5f8c7d9b4-w9k2m        1/1     Running   0          5d
jenkins-6d9f4c8a2-y3m7n      1/1     Running   0          2d

nasir@devops:~$ docker ps | grep flask-app
a1b2c3d4e5f6   flask-app:latest   "python app.py"   5 days ago   Up 5 days   0.0.0.0:5000->5000/tcp

nasir@devops:~$ terraform apply -auto-approve
aws_eks_cluster.main: Creation complete after 12m34s
Apply complete! Resources: 15 added, 0 changed, 0 destroyed.

nasir@devops:~$ ansible-playbook deploy.yml
PLAY [Deploy to Production] **********************************
TASK [Gathering Facts] *************************************** ok=[12]
TASK [Deploy App] ******************************************** ok=[12]
PLAY RECAP *************************************************** 12 ok, 0 failed

nasir@devops:~$ jenkins build ci-cd-pipeline
✅ Build #123 SUCCESS | All tests passed | Deployed to EKS
