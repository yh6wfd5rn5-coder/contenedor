#!/bin/bash
# INSTALACIÓN RÁPIDA - Contenedor Superinteligencia
# Este script configura el puente completo en tu máquina local

set -e

echo "🚀 INSTALANDO CONTENEDOR SUPERINTELIGENCIA"
echo "=========================================="
echo ""

# Verificar requisitos
echo "📋 Verificando requisitos..."

if ! command -v git &> /dev/null; then
    echo "❌ Git no está instalado"
    exit 1
fi

git_version=$(git --version | awk '{print $3}')
echo "✅ Git $git_version instalado"

# Crear directorio de instalación
INSTALL_DIR="${1:-.}"
echo ""
echo "📂 Instalando en: $INSTALL_DIR"

if [ -d "$INSTALL_DIR/contenedor" ]; then
    echo "⚠️  El directorio ya existe. Actualizando..."
    cd "$INSTALL_DIR/contenedor"
    git pull origin main
    git submodule update --remote --merge
else
    echo "📥 Clonando repositorio base..."
    cd "$INSTALL_DIR"
    git clone --recursive https://github.com/yh6wfd5rn5-coder/contenedor.git
    cd contenedor
fi

echo ""
echo "🔗 Inicializando submódulos..."
git submodule update --init --recursive
git submodule foreach git pull origin

echo ""
echo "✅ INSTALACIÓN COMPLETADA"
echo "=========================================="
echo ""
echo "📦 Estructura instalada:"
tree -L 2 2>/dev/null || find . -maxdepth 2 -type d | head -20

echo ""
echo "🚀 Próximos pasos:"
echo "  1. cd contenedor"
echo "  2. chmod +x scripts/sync.sh"
echo "  3. ./scripts/sync.sh  # Sincronizar todos los módulos"
echo ""
echo "📚 Documentación:"
echo "  - README.md       → Visión general"
echo "  - BRIDGE.md       → Guía detallada"
echo "  - bridge-config.yaml → Configuración"
echo ""
echo "🔐 Para privacidad:"
echo "  - Usar SSH: git config --global core.sshCommand 'ssh -i ~/.ssh/id_rsa'"
echo "  - O PAT: git config credential.helper store"
