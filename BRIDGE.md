# 🔗 PUENTE PRIVADO - Sistema de Integración

Este repositorio actúa como **hub centralizado** que conecta tres repositorios en un sistema integrado.

## Estructura

```
contenedor/
├── .gitmodules           # Configuración de submódulos
├── bridge-config.yaml    # Configuración del puente
├── modules/
│   ├── tanque/          # Módulo de procesamiento
│   └── nodriza/         # Módulo de superinteligencia
└── scripts/
    └── sync.sh          # Script de sincronización
```

## Repositorios Conectados

| Repo | Rol | URL |
|------|-----|-----|
| **tanque** | Procesamiento | `yenqin1ti-gif/tanque` |
| **nodriza-superinteligencia** | IA/Superinteligencia | `yh6wfd5rn5/nodriza-superinteligencia` |
| **contenedor** | Hub Central | `yh6wfd5rn5-coder/contenedor` |

## 🚀 Cómo Clonar (incluye TODOS los submódulos)

```bash
git clone --recursive https://github.com/yh6wfd5rn5-coder/contenedor.git
cd contenedor
```

O si ya clonaste sin `--recursive`:

```bash
git submodule update --init --recursive
```

## 📝 Actualizar Submódulos

```bash
# Actualizar todos
git submodule update --remote

# Actualizar uno específico
git submodule update --remote modules/tanque
```

## 🔐 Configuración de Acceso Privado

### Opción 1: SSH (Recomendado)

```bash
# Agregar clave SSH a GitHub
ssh-keygen -t ed25519 -C "tu-email@example.com"
cat ~/.ssh/id_ed25519.pub  # Copia esto a GitHub Settings

# Verificar conexión
ssh -T git@github.com
```

### Opción 2: Token PAT (Personal Access Token)

```bash
# Generar token en: GitHub → Settings → Developer Settings → Personal Access Tokens
# Usar token como contraseña al clonar
git clone https://token@github.com/yh6wfd5rn5-coder/contenedor.git
```

### Opción 3: Git Credentials

```bash
git config --global credential.helper store
# Primera vez que cones, pedirá usuario/contraseña
# Las guardará localmente (encriptado en sistemas seguros)
```

## 🔄 Sincronización Automática (GitHub Actions)

Crea `.github/workflows/sync-modules.yml`:

```yaml
name: Sincronizar Submódulos
on:
  schedule:
    - cron: '0 */6 * * *'  # Cada 6 horas
  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          submodules: true
      - run: git submodule update --remote
      - uses: EndBug/add-and-commit@v9
        with:
          message: 'chore: actualizar submódulos'
```

## 🛡️ Privacidad

✅ **Privado por defecto:**
- Acceso solo con credenciales
- Sin exposición de URLs públicas en `.gitmodules` si usas SSH
- Encriptación de tokens recomendada

⚠️ **Consideraciones:**
- Los URLs en `.gitmodules` pueden exponerse en público
- Usa SSH con claves para máxima seguridad
- Configura `.netrc` o git credentials para HTTPS

## 📚 Comandos Útiles

```bash
# Ver estado de todos los submódulos
git submodule foreach git status

# Hacer cambios en un submódulo
cd modules/tanque
git checkout feature/super-neurosis
git pull

# Actualizar el puente (contenedor) con cambios de submódulos
cd ../..
git add modules/
git commit -m "chore: actualizar referencias de submódulos"
git push
```

## 🎯 Casos de Uso

1. **Desarrollo Centralizado**: Trabaja en los 3 repos desde un solo lugar
2. **Sincronización**: Cambios automáticos en todos los módulos
3. **Versionado**: Controla qué versión de cada módulo usas
4. **Replicación**: Clona el sistema completo en otros equipos fácilmente

---

**Creado**: 2026-08-09  
**Tipo**: Puente Privado  
**Acceso**: Requiere Autenticación
