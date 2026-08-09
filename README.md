# 🌐 CONTENEDOR - Sistema Integrado de Superinteligencia

**Tu puente privado unificado que conecta 3 repositorios en un sistema coherente.**

```
🔗 ARQUITECTURA DEL PUENTE:

contenedor (HUB CENTRAL)
│
├─── 📦 tanque (Procesamiento)
│    └── URL: https://github.com/yenqin1ti-gif/tanque
│    └── Rama: feature/super-neurosis
│
└─── 🧠 nodriza-superinteligencia (IA)
     └── URL: https://github.com/yh6wfd5rn5/nodriza-superinteligencia
     └── Rama: main
```

## 🎯 ¿Qué es esto?

Un **sistema integrado privado** que actúa como contenedor central unificando:
- Procesamiento de datos (tanque)
- Inteligencia artificial (nodriza-superinteligencia)
- Orquestación y sincronización (contenedor)

**Todo funciona como uno solo, pero mantiene módulos separados.**

---

## 🚀 INSTALACIÓN RÁPIDA

### Opción 1: Instalador automático
```bash
bash INSTALL.sh
```

### Opción 2: Clonar con submódulos
```bash
git clone --recursive https://github.com/yh6wfd5rn5-coder/contenedor.git
cd contenedor
git submodule update --init --recursive
```

### Opción 3: Manual (si ya clonaste)
```bash
git clone https://github.com/yh6wfd5rn5-coder/contenedor.git
cd contenedor
git submodule update --init --recursive
```

---

## 📚 DOCUMENTACIÓN

| Archivo | Descripción |
|---------|------------|
| **README.md** | Esta documentación |
| **BRIDGE.md** | Guía técnica completa |
| **bridge-config.yaml** | Configuración centralizada |
| **.gitmodules** | Conexión de submódulos |
| **scripts/sync.sh** | Sincronización automática |
| **INSTALL.sh** | Script de instalación |

---

## 🔄 SINCRONIZACIÓN

### Sincronizar TODO automáticamente
```bash
chmod +x scripts/sync.sh
./scripts/sync.sh
```

### Sincronizar un módulo específico
```bash
# Actualizar tanque
cd modules/tanque
git pull origin feature/super-neurosis
cd ../..

# O actualizar nodriza
cd modules/nodriza
git pull origin main
cd ../..
```

### Actualizar referencias en el puente
```bash
git add modules/
git commit -m "chore: actualizar submódulos"
git push origin main
```

---

## 🛠️ DESARROLLO

### Trabajar en tanque
```bash
cd modules/tanque
git checkout feature/super-neurosis
# hacer cambios...
git add .
git commit -m "feat: descripción del cambio"
git push origin feature/super-neurosis
cd ../..
git add modules/tanque
git commit -m "chore: actualizar referencia de tanque"
git push origin main
```

### Trabajar en nodriza-superinteligencia
```bash
cd modules/nodriza
git checkout main
# hacer cambios...
git add .
git commit -m "feat: descripción del cambio"
git push origin main
cd ../..
git add modules/nodriza
git commit -m "chore: actualizar referencia de nodriza"
git push origin main
```

---

## 🔐 SEGURIDAD

### Configurar SSH (Recomendado)
```bash
ssh-keygen -t ed25519 -C "tu-email@example.com"
cat ~/.ssh/id_ed25519.pub  # Agregar a GitHub Settings
ssh -T git@github.com  # Verificar conexión
```

### O usar Token PAT
```bash
# Generar en GitHub → Settings → Developer Settings → Personal Access Tokens
# Usar como contraseña en los clones HTTPS
```

### Guardar credenciales (Git Credentials)
```bash
git config --global credential.helper store
# Pedirá credenciales primera vez, las guarda automáticamente
```

---

## 📊 ESTRUCTURA COMPLETA

```
contenedor/
├── .gitmodules                    # ← Puente de conexión (CRÍTICO)
├── README.md                      # ← Estás aquí
├── BRIDGE.md                      # Guía técnica
├── INSTALL.sh                     # Instalador
├── bridge-config.yaml             # Configuración
├── modules/
│   ├── tanque/                   # Submódulo 1: Procesamiento
│   └── nodriza/                  # Submódulo 2: IA/Superinteligencia
└── scripts/
    └── sync.sh                    # Script de sincronización
```

---

## 🎯 CASOS DE USO

### 1️⃣ Desarrollo Centralizado
Trabaja en los 3 repositorios desde un único lugar, sin cambiar URLs.

### 2️⃣ Sincronización Automática
Los cambios se propagan automáticamente entre módulos.

### 3️⃣ Versionado Unificado
Controla qué versión de cada módulo usas.

### 4️⃣ Replicación Completa
Clona el sistema completo en otros equipos con un comando.

### 5️⃣ Colaboración Privada
Sistema privado, solo acceso autorizado.

---

## 🔗 COMANDOS ÚTILES

```bash
# Ver estado de todos los submódulos
git submodule foreach git status

# Ver commits recientes en cada módulo
git submodule foreach git log --oneline -5

# Cambiar rama en un módulo
cd modules/tanque
git checkout feature/super-neurosis
cd ../..

# Eliminar cambios no committeados en un módulo
git submodule foreach git reset --hard

# Actualizar a la última versión remota
git submodule update --remote --merge

# Ver diferencias en los submódulos
git diff --submodule
```

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### El submódulo no se clona correctamente
```bash
rm -rf modules/
git submodule update --init --recursive
```

### Cambios perdidos en un módulo
```bash
cd modules/tanque
git reflog  # Ver histórico
git checkout <commit-id>  # Recuperar commit
cd ../..
```

### Permisos denegados
```bash
# Verificar acceso SSH
ssh -T git@github.com

# O usar HTTPS con token
git config credential.helper store
```

### El script sync.sh no es ejecutable
```bash
chmod +x scripts/sync.sh
./scripts/sync.sh
```

---

## 📞 SOPORTE

Para problemas específicos:
- **tanque**: Ver `modules/tanque/README.md`
- **nodriza**: Ver `modules/nodriza/README.md`
- **Sincronización**: Ver `BRIDGE.md`

---

## 📋 CHECKLIST DE INICIO

- [ ] Clonar o instalar con `INSTALL.sh`
- [ ] Verificar acceso SSH: `ssh -T git@github.com`
- [ ] Actualizar submódulos: `git submodule update --init --recursive`
- [ ] Hacer prueba de sincronización: `./scripts/sync.sh`
- [ ] Revisar estructura: `tree -L 2` o `find . -maxdepth 2 -type d`
- [ ] Leer `BRIDGE.md` para detalles técnicos

---

**Sistema creado:** 2026-08-09  
**Tipo:** Puente Privado Integrado  
**Estado:** ✅ Operacional  
**Acceso:** Solo propietarios autenticados  
**Versión:** 1.0

---

💡 **Tip:** Usa `./scripts/sync.sh` regularmente para mantener todo sincronizado.
