# 🌐 Contenedor - Hub de Integración Privada

**Sistema de puente que conecta múltiples repositorios en una arquitectura integrada.**

```
contenedor (hub central)
    ├── tanque (procesamiento)
    └── nodriza-superinteligencia (IA)
```

## 🎯 Propósito

Este repositorio actúa como **contenedor unificado** que:
- ✅ Agrupa 3 repositorios como submódulos
- ✅ Sincroniza automáticamente cambios
- ✅ Mantiene todo privado y encriptado
- ✅ Facilita clonación y replicación del sistema completo

## 📦 Instalación Rápida

```bash
# Clonar con todos los submódulos
git clone --recursive https://github.com/yh6wfd5rn5-coder/contenedor.git
cd contenedor

# O si ya existe
git submodule update --init --recursive
```

## 🔗 Repositorios Integrados

| Nombre | Función | Estado |
|--------|---------|--------|
| **tanque** | Módulo de procesamiento de datos | 🟢 Conectado |
| **nodriza-superinteligencia** | Motor de IA y superinteligencia | 🟢 Conectado |

## 📚 Documentación Completa

- Ver [`BRIDGE.md`](BRIDGE.md) para detalles técnicos
- Ver [`bridge-config.yaml`](bridge-config.yaml) para configuración
- Ver [`scripts/sync.sh`](scripts/sync.sh) para sincronización manual

## 🚀 Uso

### Actualizar todo
```bash
./scripts/sync.sh
```

### Actualizar un módulo específico
```bash
git submodule update --remote modules/tanque
```

### Trabajar en un módulo
```bash
cd modules/tanque
git checkout feature/super-neurosis
git pull
# Hacer cambios...
git push
cd ../..
git add modules/tanque
git commit -m "update: cambios en tanque"
```

## 🔐 Seguridad

- 🔒 Repositorio privado
- 🔑 Acceso mediante SSH o PAT
- 🛡️ Encriptación de credenciales
- 📋 Control de acceso basado en roles

## ⚙️ Sincronización Automática

GitHub Actions ejecuta sincronización cada 6 horas.  
Trigger manual disponible en Actions → "Sincronizar Submódulos"

## 📋 Requisitos

- Git 2.13+
- Acceso SSH o PAT a los repositorios
- Bash (para scripts)

## 🤝 Contribuir

1. Hacer cambios en los módulos
2. Actualizar referencias: `git add modules/`
3. Commit: `git commit -m "update: descripción"`
4. Push: `git push`

---

**Tipo**: Puente Privado  
**Acceso**: Solo propietarios autenticados  
**Sincronización**: Automática cada 6 horas
