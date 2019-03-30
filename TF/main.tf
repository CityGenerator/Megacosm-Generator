provider "kubernetes" {}

resource "kubernetes_namespace" "megacosm" {
  metadata {
    name = "megacosm"
  }
}


resource "kubernetes_deployment" "megacosm-deployment" {
  metadata {
    name = "megacosm-deployment"
    labels {
      test = "Megacosm"
    }
  }

  spec {
    replicas = 2

    selector {
      match_labels {
        test = "Megacosm"
      }
    }

    template {
      metadata {
        labels {
          test = "Megacosm"
        }
      }
      spec {
        container {
          image = "redis:latest"
          name  = "redis"
          resources{
            limits{
              cpu    = "0.5"
              memory = "512Mi"
            }
            requests{
              cpu    = "250m"
              memory = "50Mi"
            }
          }
        }
        container {
          image="python:3.7"
          name = "data-loader"
        }
      }
    }
  }
}



//resource "kubernetes_service" "redis-service" {
//  metadata {
//    name = "redis-service"
//  }
//  spec {
//    selector {
//      app = "${kubernetes_pod.redis.metadata.0.labels.app}"
//    }
//    session_affinity = "ClientIP"
//    port {
//      port = 16379
//      target_port = 6379
//    }
//
//    type = "LoadBalancer"
//  }
//}

resource "kubernetes_pod" "megacosm" {
  metadata {
    name = "megacosm"
    labels {
      app = "Megacosm"
    }
  }

  spec {
    container {
      image = "redis:latest"
      name  = "redis"
    }
    container {
      image = "python"
      name  = "redis"
    }
  }
}

