#!/bin/bash
# Script de sincronización automática del puente
# Uso: ./scripts/sync.sh

set -e

echo "🔄 SINCRONIZANDO PUENTE PRIVADO..."
echo "=================================="

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Función de log
log() {
    echo -e "${GREEN}[✓]${NC} $1"
}

error() {
    echo -e "${RED}[✗]${NC} $1"
    exit 1
}

warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

# Verificar que estamos en la raíz del repo
if [ ! -f ".gitmodules" ]; then
    error "No se encontró .gitmodules. Ejecuta desde la raíz del repositorio."
fi

log "Actualizando submódulos..."
git submodule update --remote --merge || warning "Actualización de submódulos completada con advertencias"

log "Obteniendo cambios de tanque..."
cd modules/tanque
git fetch origin
git checkout feature/super-neurosis
git pull
cd ../..

log "Obteniendo cambios de nodriza..."
cd modules/nodriza
git fetch origin
git checkout main
git pull
cd ../..

log "Registrando cambios en el puente..."
git add -A
git commit -m "chore: sincronizar submódulos [$(date +'%Y-%m-%d %H:%M:%S')]" || log "No hay cambios nuevos"

log "Enviando cambios..."
git push origin main || warning "Push completado con advertencias"

echo ""
echo -e "${GREEN}=================================="
echo "✨ SINCRONIZACIÓN COMPLETADA"
echo "==================================${NC}"

# Mostrar estado
echo ""
echo "Estado actual:"
git submodule foreach 'echo "  → $name: $(git rev-parse --short HEAD)"'
