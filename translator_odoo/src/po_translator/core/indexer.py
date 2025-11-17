"""Module indexer for linking PO entries to their source modules"""
from po_translator.utils.file_utils import extract_module_name


class ModuleIndexer:
    """Index and track which module, model, and field each PO entry belongs to"""
    
    def __init__(self):
        self.entry_to_module = {}
        self.entry_to_model = {}  # Store model information (e.g., ir.model.fields)
        self.entry_to_field = {}  # Store full field path (e.g., test_module.field_sale_order__name)
        self.entry_to_occurrence = {}  # Store full occurrence string
        self.module_to_entries = {}
    
    def index_entry(self, entry_id, filepath, entry=None):
        """
        Index an entry with its source module and model
        
        Args:
            entry_id: Unique identifier for entry (msgid)
            filepath: Path to source .po file
            entry: POEntry object (optional, to extract module/model from metadata)
        """
        # Try to extract module from entry comment first
        module_name = 'unknown'
        model_info = None
        
        if entry and hasattr(entry, 'comment') and entry.comment:
            # Look for "module: module_name" in comment
            import re
            match = re.search(r'module:\s*(\w+)', entry.comment)
            if match:
                module_name = match.group(1)
        
        # Fallback to filepath extraction
        if module_name == 'unknown':
            module_name = extract_module_name(filepath)
        
        # Extract model and field information from occurrences
        if entry and hasattr(entry, 'occurrences') and entry.occurrences:
            for occ_file, occ_line in entry.occurrences:
                if 'model:' in occ_file:
                    # Store full occurrence for reference
                    self.entry_to_occurrence[entry_id] = occ_file
                    
                    # Parse "model:ir.model.fields,field_description:test_module.field_sale_order__name"
                    parts = occ_file.split(':')
                    if len(parts) >= 2:
                        # Extract model (e.g., "ir.model.fields")
                        model_parts = parts[1].split(',')
                        if model_parts:
                            model_info = model_parts[0]
                    
                    # Extract field path if present
                    if len(parts) >= 3:
                        field_path = parts[2]  # e.g., "test_module.field_sale_order__name"
                        self.entry_to_field[entry_id] = field_path
                    
                    break
        
        self.entry_to_module[entry_id] = module_name
        
        if model_info:
            self.entry_to_model[entry_id] = model_info
        
        if module_name not in self.module_to_entries:
            self.module_to_entries[module_name] = []
        
        if entry_id not in self.module_to_entries[module_name]:
            self.module_to_entries[module_name].append(entry_id)
    
    def get_module(self, entry_id):
        """
        Get module name for an entry
        
        Args:
            entry_id: Entry identifier
            
        Returns:
            str: Module name or 'unknown'
        """
        return self.entry_to_module.get(entry_id, 'unknown')
    
    def get_model(self, entry_id):
        """
        Get model information for an entry
        
        Args:
            entry_id: Entry identifier
            
        Returns:
            str: Model name (e.g., 'ir.model.fields', 'ir.ui.view') or None
        """
        return self.entry_to_model.get(entry_id)
    
    def get_field(self, entry_id):
        """
        Get field path for an entry
        
        Args:
            entry_id: Entry identifier
            
        Returns:
            str: Field path (e.g., 'test_module.field_sale_order__name') or None
        """
        return self.entry_to_field.get(entry_id)
    
    def get_occurrence(self, entry_id):
        """
        Get full occurrence string for an entry
        
        Args:
            entry_id: Entry identifier
            
        Returns:
            str: Full occurrence (e.g., 'model:ir.model.fields,field_description:...') or None
        """
        return self.entry_to_occurrence.get(entry_id)
    
    def get_module_and_model(self, entry_id):
        """
        Get both module and model for an entry
        
        Args:
            entry_id: Entry identifier
            
        Returns:
            tuple: (module_name, model_name) where model_name may be None
        """
        module = self.get_module(entry_id)
        model = self.get_model(entry_id)
        return module, model
    
    def get_full_info(self, entry_id):
        """
        Get complete information for an entry
        
        Args:
            entry_id: Entry identifier
            
        Returns:
            dict: {
                'module': str,
                'model': str or None,
                'field': str or None,
                'occurrence': str or None
            }
        """
        return {
            'module': self.get_module(entry_id),
            'model': self.get_model(entry_id),
            'field': self.get_field(entry_id),
            'occurrence': self.get_occurrence(entry_id)
        }
    
    def get_entries_by_module(self, module_name):
        """
        Get all entries for a module
        
        Args:
            module_name: Name of module
            
        Returns:
            list: List of entry IDs
        """
        return self.module_to_entries.get(module_name, [])
    
    def get_all_modules(self):
        """
        Get list of all indexed modules
        
        Returns:
            list: Sorted list of module names
        """
        return sorted(self.module_to_entries.keys())
    
    def clear(self):
        """Clear all indexed data"""
        self.entry_to_module.clear()
        self.entry_to_model.clear()
        self.entry_to_field.clear()
        self.entry_to_occurrence.clear()
        self.module_to_entries.clear()

